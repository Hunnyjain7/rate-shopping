import {
  CssBaseline,
  Box,
  Container,
  FormControl,
  InputLabel,
  InputAdornment,
  Typography,
  IconButton,
  Button,
  Link,
} from "@mui/material";
import { Visibility, VisibilityOff } from "@mui/icons-material";
import { useState, FormEvent, Fragment } from "react";
import BootstrapInput from "../styles/bootstrapInput";
import { clientLogin, adminLogin } from "../services/apiEndpoints";
import ApiAlert from "../helpers/alert";
import SignInFormElement from "../interfaces/signInForm";

const SignIn = (app: any) => {
  const [showPassword, setShowPassword] = useState(false);
  const [apiError, setApiError] = useState(null);

  const handleTogglePasswordVisibility = () => {
    setShowPassword((prevShowPassword) => !prevShowPassword);
  };

  const dashboardUrl = app.isAdminSubdomain
    ? "/admin-dashboard"
    : "/client-dashboard";

  const handleSubmit = async (event: FormEvent<SignInFormElement>) => {
    event.preventDefault();
    const formElements = event.currentTarget.elements;
    const data = {
      email: formElements.email.value,
      password: formElements.password.value,
    };

    const resData: any = app.isAdminSubdomain
      ? await adminLogin(data)
      : await clientLogin(data);
    console.log("resData", resData);

    if (resData.error) {
      setApiError(resData.error);
    } else if (resData.data.status === "success") {
      window.location.href = dashboardUrl;
    }
  };

  return (
    <Fragment>
      <CssBaseline />
      <Container maxWidth="xl" disableGutters>
        {apiError && (
          <ApiAlert
            severity="error"
            message={apiError}
            onClose={() => {
              setApiError(null);
            }}
          />
        )}
        <Box sx={{ display: "flex", height: "100vh" }}>
          <Box
            sx={{
              flex: 1,
              display: "flex",
              backgroundColor: "#cfe8fc",
            }}
          >
            <img
              src="https://picsum.photos/743/708"
              alt="Rate Shopping"
              loading="lazy"
            />
          </Box>

          <Box
            sx={{
              flex: 1,
              display: "flex",
            }}
          >
            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                flexFlow: "wrap",
              }}
            >
              <Box>
                <Typography
                  variant="body2"
                  gutterBottom
                  sx={{
                    marginTop: "-50px",
                    marginLeft: "400px",
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
              </Box>
              <Typography variant="h2" gutterBottom>
                Rate Shopping
              </Typography>
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  flexFlow: "wrap",
                }}
              >
                <form onSubmit={handleSubmit}>
                  <Box
                    sx={{
                      justifyContent: "center",
                      flexDirection: "column",
                      display: "flex",
                    }}
                  >
                    <Typography variant="h5" gutterBottom>
                      {app.app}
                    </Typography>

                    <FormControl variant="standard" required>
                      <InputLabel shrink htmlFor="bootstrap-input">
                        Email address
                      </InputLabel>
                      <BootstrapInput
                        name="email"
                        type="email"
                        id="bootstrap-input"
                      />
                    </FormControl>
                    <FormControl
                      required
                      sx={{
                        marginTop: "5px",
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
                          name="password"
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
                        type="submit"
                        sx={{
                          width: "50%",
                          borderRadius: "25px",
                          backgroundColor: "rgba(0, 0, 0, 0.4)",
                          fontFamily: "Roboto,Helvetica,Arial,sans-serif",
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
                </form>
              </Box>
            </Box>
          </Box>
        </Box>
      </Container>
    </Fragment>
  );
};

export default SignIn;
