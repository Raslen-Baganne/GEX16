import React from 'react';
import { useNavigate } from 'react-router-dom';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import './AdminHeader.css';

const AdminHeader = () => {
  const navigate = useNavigate();

  return (
    <header className="header">
      <div className="header-left">
        <div className="logo-container">
          <i className="pi pi-chart-bar"></i>
          <i className="pi pi-chart-line logo-overlay"></i>
        </div>
        <span className="brand-name">GexFME</span>
      </div>
      <div className="header-right">
        <a className="header-link home-icon" onClick={() => navigate('/admin-dashboard')}>
          <i className="pi pi-home"></i>
        </a>
        <a href="#" className="header-link support">
          <div className="support-icon-container">
            <i className="pi pi-headset"></i>
            <i className="pi pi-comments support-icon-overlay"></i>
          </div>
          <span>Support</span>
        </a>
      </div>
    </header>
  );
};

export default AdminHeader;
