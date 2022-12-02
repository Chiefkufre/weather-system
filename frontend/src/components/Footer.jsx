import React from 'react';
import { Link } from 'react-router-dom';
import { BsGlobe } from 'react-icons/bs';
import { BiSupport } from 'react-icons/bi';
import { useTranslation } from 'react-i18next';

export default function Footer() {
  const { t } = useTranslation(['common']);

  return (
    <footer className="self-end pt-16 text-white bg-primary-btn-clicked">
      <div className="p-4 bg-[#B93815] md:py-10 md:px-16">
        <div className="flex flex-col gap-10 pb-12 md:flex-row md:justify-between md:items-center">
          <div>
            <img src="/logo-white.png" alt="logo" />
            <div className="flex flex-col flex-wrap gap-6 mt-8 md:flex-row">
              <Link to="/about-us" className="link link-hover">{t('aboutus')}</Link>
              {/* <Link to="/promotions" className="link link-hover">Promotions</Link> */}
            </div>
          </div>
          <div>
            <span className="footer-title">{t('downloadtheapp')}</span>
            <div className="flex flex-wrap gap-6 mt-6">
              <img src="/app-store.png" alt="app store" />
              <img src="/google-play.png" alt="google play" />
            </div>
          </div>
        </div>
        <div className="flex flex-col justify-between gap-4 pt-5 border-t border-t-white md:flex-row">
          <p className="order-last text-sm md:order-first md:text-base">{t('allrights')}</p>
          <div className="flex gap-6">
            <span className="flex items-center gap-2">
              <BsGlobe />
              <span className="hidden md:block">English</span>
            </span>
            <span className="flex items-center gap-2">
              <img src="/icons/uk-flag.png" alt="uk flag" />
              <span className="hidden md:block">United Kingdom</span>
            </span>
            <span className="flex items-center gap-2">
              <BiSupport />
              <span className="hidden md:block">Customer Support</span>
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
}
