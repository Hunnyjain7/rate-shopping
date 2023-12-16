import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";

import InputLabel from "@mui/material/InputLabel";
import FormControl from "@mui/material/FormControl";
import Typography from "@mui/material/Typography";
import InputAdornment from "@mui/material/InputAdornment";
import IconButton from "@mui/material/IconButton";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import Button from "@mui/material/Button";
import { Link } from "@mui/material";
import { useState } from "react";
import React from "react";
import BootstrapInput from "../styles/bootstrapInput";

const SignIn = (app: any) => {
  const [showPassword, setShowPassword] = useState(false);

  const handleTogglePasswordVisibility = () => {
    setShowPassword((prevShowPassword) => !prevShowPassword);
  };
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="xl" disableGutters>
        <Box sx={{ display: "flex", height: "100vh" }}>
          <Box sx={{ flex: 1, backgroundColor: "#cfe8fc" }} />

          <Box
            sx={{
              flex: 1,
              display: "flex",
              flexDirection: "column",
              height: "85vh",
              justifyContent: "center",
              alignItems: "center",
              flexFlow: "wrap",
            }}
          >
            <Typography
              variant="body2"
              gutterBottom
              sx={{
                marginTop: "-30px",
                marginRight: "-190px",
              }}
            >
              Don't have an account?{" "}
              <Link
                id="bootstrap-input"
                component="button"
                variant="body2"
                sx={{
                  lineHeight: "2.43",
                  letterSpacing: "0.01071em",
                  color: "black",
                  textDecoration: "underline",
                }}
                onClick={() => {
                  console.info("Forgot your password button.");
                }}
              >
                Sign up
              </Link>
            </Typography>
            <Box
              sx={{
                justifyContent: "center",
                alignItems: "center",
                flexDirection: "column",
                display: "flex",
                width: "100%",
              }}
            >
              <Box
                sx={{
                  width: "57%",
                }}
              >
                <Typography className="w6" variant="h5" gutterBottom>
                  {app.app}
                </Typography>
              </Box>

              <FormControl variant="standard">
                <InputLabel shrink htmlFor="bootstrap-input">
                  User name or email address
                </InputLabel>
                <BootstrapInput defaultValue="" id="bootstrap-input" />
              </FormControl>

              <br />

              <FormControl
                sx={{
                  marginLeft: "5px",
                }}
                variant="standard"
              >
                <Box
                  sx={{
                    display: "flex",
                    alignItems: "center",
                    flexDirection: "column",
                  }}
                >
                  <Box
                    sx={{
                      justifyContent: "center",
                      alignItems: "center",
                      flexDirection: "column",
                      display: "flex",
                      width: "100%",
                    }}
                  >
                    <InputLabel shrink htmlFor="bootstrap-input">
                      Your password
                    </InputLabel>
                    <Box
                      sx={{
                        marginRight: "20px",
                        padding: "0px",
                        marginInlineStart: "auto",
                      }}
                    >
                      <IconButton
                        onClick={handleTogglePasswordVisibility}
                        edge="end"
                        sx={{
                          marginRight: "5px",
                          padding: "0px",
                          marginInlineStart: "auto",
                          marginBottom: "5px",
                        }}
                      >
                        {showPassword ? (
                          <Visibility fontSize="small" />
                        ) : (
                          <VisibilityOff fontSize="small" />
                        )}
                      </IconButton>
                      <label id="hide-lable" htmlFor="bootstrap-input">
                        Hide
                      </label>
                    </Box>
                  </Box>

                  <BootstrapInput
                    id="bootstrap-input"
                    type={showPassword ? "text" : "password"}
                    endAdornment={
                      <InputAdornment position="end"></InputAdornment>
                    }
                  />
                  <Link
                    id="bootstrap-input"
                    component="button"
                    variant="body2"
                    sx={{
                      lineHeight: "2.43",
                      letterSpacing: "0.01071em",
                      color: "black",
                      textDecoration: "underline",
                      textDecorationColor: "",
                      fontSize: "-0.125rem",
                      marginLeft: "auto",
                      marginRight: "7.5px",
                    }}
                    onClick={() => {
                      console.info("Forgot your password button.");
                    }}
                  >
                    Forgot your password
                  </Link>
                </Box>
                <Button
                  id="bootstrap-input"
                  variant="contained"
                  size="large"
                  sx={{
                    width: "50%",
                    borderRadius: "25px",
                    backgroundColor: "rgba(0, 0, 0, 0.4)",
                    fontFamily: "Roboto,Helvetica,Arial,sans-serif",
                  }}
                  onClick={() => {
                    console.log("Signed IN");
                  }}
                >
                  Sign In
                </Button>
                <Typography variant="body2" gutterBottom>
                  Don't have an account?{" "}
                  <Link
                    id="bootstrap-input"
                    component="button"
                    variant="body2"
                    sx={{
                      lineHeight: "2.43",
                      letterSpacing: "0.01071em",
                      color: "black",
                      textDecoration: "underline",
                    }}
                    onClick={() => {
                      console.info("Forgot your password button.");
                    }}
                  >
                    Sign up
                  </Link>
                </Typography>
              </FormControl>
            </Box>
          </Box>
        </Box>
      </Container>
    </React.Fragment>
  );
};

export default SignIn;
