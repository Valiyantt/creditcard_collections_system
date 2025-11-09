import { Outlet, NavLink } from "react-router-dom";
import { useState } from "react";
import { Menu, X, LayoutDashboard, FileText, BarChart3, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";

const navItems = [
  { name: "Dashboard", path: "/", icon: <LayoutDashboard size={18} /> },
  { name: "Collections", path: "/collections", icon: <FileText size={18} /> },
  { name: "Reports", path: "/reports", icon: <BarChart3 size={18} /> },
  { name: "Settings", path: "/settings", icon: <Settings size={18} /> },
];

export default function DashboardLayout() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <div className="flex h-screen bg-gray-50 text-gray-900">
      {/* Sidebar */}
      <aside
        className={`${
          isSidebarOpen ? "w-64" : "w-16"
        } bg-white border-r border-gray-200 transition-all duration-300 flex flex-col`}
      >
        <div className="text-2xl font-bold tracking-tight text-blue-600">
          <h1 className={`font-semibold text-lg ${!isSidebarOpen && "hidden"}`}>
            Altruist
          </h1>
          <Button
            variant="ghost"
            size="icon"
            className="md:hidden"
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
          >
            {isSidebarOpen ? <X size={18} /> : <Menu size={18} />}
          </Button>
        </div>

        <nav className="flex-1 overflow-y-auto px-3 py-4">
          {navItems.map((item) => (
            <NavLink
              key={item.name}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                  isActive
                    ? "bg-blue-100 text-blue-700"
                    : "text-gray-600 hover:bg-gray-100 hover:text-gray-900"
                }`
              }
            >
              {item.icon}
              {isSidebarOpen && <span>{item.name}</span>}
            </NavLink>
          ))}
        </nav>
      </aside>

      {/* Main Content */}
      <div className="flex flex-col flex-1">
        {/* Top Navbar */}
        <header className="h-14 bg-white border-b border-gray-200 flex items-center justify-between px-6">
          <div className="flex items-center gap-3">
            <Button
              variant="ghost"
              size="icon"
              className="hidden md:inline-flex"
              onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            >
              {isSidebarOpen ? <X size={18} /> : <Menu size={18} />}
            </Button>
            <h2 className="text-sm font-medium text-gray-700">Dashboard</h2>
          </div>

          <div className="flex items-center gap-3">
            <Avatar>
              <AvatarFallback>FA</AvatarFallback>
            </Avatar>
            <span className="text-sm font-medium">Franz Alverio</span>
          </div>
        </header>

        {/* Routed Pages */}
        <main className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
