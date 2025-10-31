import { jsx as _jsx } from "react/jsx-runtime";
import { AuthProvider } from "@/contexts/AuthContext";
import Login from "@/pages/auth/Login";
import Register from "@/pages/auth/Register";
import DashboardLayout from "@/layouts/DashboardLayout";
import Overview from "@/pages/dashboard/Overview";
import Collections from "@/pages/dashboard/Collections";
import Reports from "@/pages/dashboard/Reports";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import ReactDOM from "react-dom/client";
import React from "react";
import "./index.css";
const router = createBrowserRouter([
    { path: "/", element: _jsx(Login, {}) },
    { path: "/login", element: _jsx(Login, {}) },
    { path: "/register", element: _jsx(Register, {}) },
    {
        path: "/dashboard",
        element: _jsx(DashboardLayout, {}),
        children: [
            { path: "", element: _jsx(Overview, {}) },
            { path: "collections", element: _jsx(Collections, {}) },
            { path: "reports", element: _jsx(Reports, {}) },
        ],
    },
]);
ReactDOM.createRoot(document.getElementById("root")).render(_jsx(React.StrictMode, { children: _jsx(AuthProvider, { children: _jsx(RouterProvider, { router: router }) }) }));
