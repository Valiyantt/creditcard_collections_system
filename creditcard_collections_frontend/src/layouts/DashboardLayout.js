import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { Outlet, NavLink } from "react-router-dom";
import { useState } from "react";
import { Menu, X, LayoutDashboard, FileText, BarChart3, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
const navItems = [
    { name: "Dashboard", path: "/", icon: _jsx(LayoutDashboard, { size: 18 }) },
    { name: "Collections", path: "/collections", icon: _jsx(FileText, { size: 18 }) },
    { name: "Reports", path: "/reports", icon: _jsx(BarChart3, { size: 18 }) },
    { name: "Settings", path: "/settings", icon: _jsx(Settings, { size: 18 }) },
];
export default function DashboardLayout() {
    const [isSidebarOpen, setIsSidebarOpen] = useState(true);
    return (_jsxs("div", { className: "flex h-screen bg-gray-50 text-gray-900", children: [_jsxs("aside", { className: `${isSidebarOpen ? "w-64" : "w-16"} bg-white border-r border-gray-200 transition-all duration-300 flex flex-col`, children: [_jsxs("div", { className: "flex items-center justify-between p-4 border-b border-gray-100", children: [_jsx("h1", { className: `font-semibold text-lg ${!isSidebarOpen && "hidden"}`, children: "CollectionsSys" }), _jsx(Button, { variant: "ghost", size: "icon", className: "md:hidden", onClick: () => setIsSidebarOpen(!isSidebarOpen), children: isSidebarOpen ? _jsx(X, { size: 18 }) : _jsx(Menu, { size: 18 }) })] }), _jsx("nav", { className: "flex-1 overflow-y-auto px-3 py-4", children: navItems.map((item) => (_jsxs(NavLink, { to: item.path, className: ({ isActive }) => `flex items-center gap-3 px-3 py-2 rounded-md text-sm font-medium transition-colors ${isActive
                                ? "bg-blue-100 text-blue-700"
                                : "text-gray-600 hover:bg-gray-100 hover:text-gray-900"}`, children: [item.icon, isSidebarOpen && _jsx("span", { children: item.name })] }, item.name))) })] }), _jsxs("div", { className: "flex flex-col flex-1", children: [_jsxs("header", { className: "h-14 bg-white border-b border-gray-200 flex items-center justify-between px-6", children: [_jsxs("div", { className: "flex items-center gap-3", children: [_jsx(Button, { variant: "ghost", size: "icon", className: "hidden md:inline-flex", onClick: () => setIsSidebarOpen(!isSidebarOpen), children: isSidebarOpen ? _jsx(X, { size: 18 }) : _jsx(Menu, { size: 18 }) }), _jsx("h2", { className: "text-sm font-medium text-gray-700", children: "Dashboard" })] }), _jsxs("div", { className: "flex items-center gap-3", children: [_jsx(Avatar, { children: _jsx(AvatarFallback, { children: "FA" }) }), _jsx("span", { className: "text-sm font-medium", children: "Franz Alverio" })] })] }), _jsx("main", { className: "flex-1 overflow-y-auto p-6", children: _jsx(Outlet, {}) })] })] }));
}
