import { AuthProvider } from "@/contexts/AuthContext"
import Login from "@/pages/auth/Login"
import Register from "@/pages/auth/Register"
import DashboardLayout from "@/layouts/DashboardLayout"
import Overview from "@/pages/dashboard/Overview"
import Collections from "@/pages/dashboard/Collections"
import Reports from "@/pages/dashboard/Reports"
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import ReactDOM from "react-dom/client"
import React from "react"
import "./index.css"

const router = createBrowserRouter([
  { path: "/", element: <Login /> },
  { path: "/login", element: <Login /> },
  { path: "/register", element: <Register /> },
  {
    path: "/dashboard",
    element: <DashboardLayout />,
    children: [
      { path: "", element: <Overview /> },
      { path: "collections", element: <Collections /> },
      { path: "reports", element: <Reports /> },
    ],
  },
])

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
  </React.StrictMode>
)
