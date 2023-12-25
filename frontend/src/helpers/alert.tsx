import React, { useState, useEffect } from "react";
import Alert from "@mui/material/Alert";

interface AlertProps {
  severity: "success" | "info" | "warning" | "error";
  message: string;
  onClose: () => void;
}

const ApiAlert: React.FC<AlertProps> = ({ severity, message, onClose }) => {
  const [open, setOpen] = useState(true);

  useEffect(() => {
    // Automatically close the alert after a certain duration (e.g., 5 seconds)
    const timeoutId = setTimeout(() => {
      setOpen(false);
      onClose();
    }, 5000);

    // Clear the timeout if the component unmounts or if the alert is manually closed
    return () => clearTimeout(timeoutId);
  }, [onClose]);

  return (
    <div style={{ position: "fixed", top: 20, right: 20, zIndex: 9999 }}>
      {open && (
        <Alert
          severity={severity}
          onClose={() => {
            setOpen(false);
            onClose();
          }}
        >
          {message}
        </Alert>
      )}
    </div>
  );
};

export default ApiAlert;
