import React from 'react';
import './Notification.css';

const Notification = ({ message, type = 'info', onClose }) => {
  if (!message) return null;

  return (
    <div className={`notification ${type}`}>
      <span>{message}</span>
      <button className="notification-close" onClick={onClose}>×</button>
    </div>
  );
};

export default Notification;
