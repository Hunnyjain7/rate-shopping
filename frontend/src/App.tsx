import { useEffect, useState } from "react";
import "./App.css";
// import * as React from "react";
import SignIn from "./components/signIn";

function App() {
  const isAdminSubdomain = window.location.hostname === "admin.localhost";
  const [app, setApp] = useState("Sign in");

  useEffect(() => {
    isAdminSubdomain ? setApp("Admin Sign in") : setApp("Sign in");
  }, [isAdminSubdomain]);

  return (
    <>
      <div className="App">
        <SignIn app={app} />
      </div>
    </>
  );
}

export default App;
