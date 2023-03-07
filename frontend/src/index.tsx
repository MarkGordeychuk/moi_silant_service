import React from "react";
import ReactDOM from "react-dom/client";
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";

import Root, { loader as RootLoader } from "./routes/Root";
import Auth from "./routes/Auth";
import Main, { loader as MainLoader } from "./routes/Main";
import Maintenances, { loader as MaintenancesLoader } from "./routes/Maintenances";
import Complaints, { loader as ComplaintsLoader } from "./routes/Complaints";
import Directory, { loader as DirectoryLoader } from "./routes/Directory";

import "./styles/style.sass";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root />,
        loader: RootLoader,
        children: [
            {
                path: "/",
                element: <Main />,
                loader: MainLoader,
            },
            {
                path: "/auth/",
                element: <Auth />,
            },
            {
                path: "/maintenances/",
                element: <Maintenances />,
                loader: MaintenancesLoader,
            },
            {
                path: "/complaints/",
                element: <Complaints />,
                loader: ComplaintsLoader,
            },
            {
                path: "/directory/:id/",
                element: <Directory />,
                loader: DirectoryLoader,
            },
        ]
    }
]);

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);