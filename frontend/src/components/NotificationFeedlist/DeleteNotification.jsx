/* eslint-disable react/prop-types */
/* eslint-disable react/no-unescaped-entities */
export default function DeleteNotification({ show, closeModal, emptyNotification }) {
  return (
    <div
      className={show ? 'notificaton_feed-delecon' : 'notificaton_feed-none'}
    >
      <div className="notificaton_feed-dele">
        <h1 className="notificatin_feed-hd">Are you sure?</h1>
        <p>
          Are you sure you want to empty your notifications. You'll lose access
          to them
        </p>
        <div className="notificaton_feed-btnflex">
          <button
            className="notificaton_feed-btn notificaton_feed-cancel"
            type="button"
            onClick={closeModal}
          >
            Cancel
          </button>
          <button
            className="notificaton_feed-btn notificaton_feed-empty"
            type="button"
            onClick={emptyNotification}
          >
            Empty now
          </button>
        </div>
      </div>
    </div>
  );
}
