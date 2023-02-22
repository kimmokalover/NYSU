import React from "react";
// import axios from "axios";

import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";

import Button from "@mui/material/Button";

import "./Main.scss";

export default function MainPageContainer() {
  const [data, setData] = React.useState({
    license_plate: "",
    name: "",
    age: "",
    address: "",
    contact_number: "",
    first_responder: "",
    vehicle_type: "",
    email: "",
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setData({
      ...data,
      [name]: value,
    });
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    console.log(data);
  };

  return (
    <div className="MainPageContainer">
      <div className="TitleContainer">
        <form onSubmit={handleSubmit}>
          <Grid
            container
            direction="column"
            justifyContent="center"
            alignItems="center"
            spacing={1}
            width="100vw"
            height="100vh"
          >
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="License Code"
                  inputProps={{ "aria-label": "license_plate" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Name"
                  inputProps={{ "aria-label": "name" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Age"
                  inputProps={{ "aria-label": "age" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Address"
                  inputProps={{ "aria-label": "address" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Phone Number"
                  inputProps={{ "aria-label": "contact_number" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Emergency Phone Number"
                  inputProps={{ "aria-label": "first_responder" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Vehicle Type"
                  inputProps={{ "aria-label": "vehicle_type" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Paper sx={{ width: "20vw", height: "5vh", borderRadius: 3 }}>
                <InputBase
                  sx={{ ml: 1, flex: 1 }}
                  placeholder="Email Address"
                  inputProps={{ "aria-label": "email" }}
                  onChange={handleInputChange}
                />
              </Paper>
            </Grid>
            <Grid item>
              <Button
                type="submit"
                sx={{ color: "black", fontWeight: "bold", fontSize: "2vw" }}
              >
                Send
              </Button>
            </Grid>
          </Grid>
        </form>
      </div>
    </div>
  );
}
