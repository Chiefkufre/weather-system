import pytest
from app.utils.general import (compose_location, convert_epoch_to_datetime,
                               decompose_merged_location, get_weather_forecast,
                               weather_api_call)
from fastapi import HTTPException


@pytest.mark.parametrize(
    "city, state, country, expected",
    [
        ("a", "b", "c", "a-b-c"),
        ("a", "b", "c d", "a-b-c d"),
    ]
)
def test_compose_location(city, state, country, expected):
    assert compose_location(
        city, state, country
    ) == expected


@pytest.mark.parametrize(
    "merged, expected",
    [
        ("a-b-c", {
            "city": "a",
            "state": "b",
            "country": "c"
        }),
        ("a-b-c d", {
            "city": "a",
            "state": "b",
            "country": "c d"
        }),
        ("a d-b-c d", {
            "city": "a d",
            "state": "b",
            "country": "c d"
        }),
    ]
)
def test_decompose_merged_location(merged, expected):
    assert decompose_merged_location(merged) == expected


def test_convert_epoch_to_datetime():
    epoch_time = 1612904800
    expected = {
        "date": "09 Feb, 2021",
        "time": "10:06pm"
    }
    assert convert_epoch_to_datetime(epoch_time) == expected


def test_weather_api_call(mocker):
    mocker.patch('app.utils.general.requests.get', return_value=mocker.Mock(
        status_code=200,
        json=lambda: {
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "dt": 1661870592,
            "timezone": 7200,
        }
    ))

    expected = {
        "dt": 1661870592,
        "main": "Rain",
        "description": "moderate rain",
    }
    assert weather_api_call(1, 1) == expected


def test_weather_api_call_error(mocker):
    mocker.patch('app.utils.general.requests.get', return_value=mocker.Mock(
        status_code=400,
    ))
    with pytest.raises(HTTPException):
        weather_api_call(1, 1)


class TestGetWeatherForecast:
    def test_weather_forcasts_valid(self, mocker):
        """Test weather forecast endpoint"""
        # mocker request.get json response
        mocker.patch(
            'requests.get',
            return_value=mocker.Mock(
                status_code=200,
                json=mocker.Mock(
                    return_value={
                        "cod": "200",
                        "message": 0,
                        "cnt": 40,
                        "list": [
                            {
                                "test": "demo"
                            },
                        ]
                    }
                )
            )
        )

        results = get_weather_forecast(6.5244, 3.3792)
        assert results == [{"test": "demo"}]

    @pytest.mark.parametrize(
        "cod",
        [
            "400",
            "401",
        ]
    )
    def test_weather_forcasts_invalid(self, cod, mocker):
        """Test weather forecast endpoint"""
        # mocker request.get json response
        mocker.patch(
            'requests.get',
            return_value=mocker.Mock(
                status_code=200,
                json=mocker.Mock(
                    return_value={
                        "cod": cod,
                        "message": 0,
                        "cnt": 40,
                        "list": [
                            {
                                "test": "demo"
                            },
                        ]
                    }
                )
            )
        )

        with pytest.raises(Exception):
            get_weather_forecast(6.5244, 3.3792)

    def test_weather_forcasts_error(self, mocker):
        """Test weather forecast endpoint"""
        mocker.patch(
            'requests.get',
            return_value=mocker.Mock(
                status_code=400
            )
        )

        with pytest.raises(Exception):
            get_weather_forecast(6.5244, 3.3792)
