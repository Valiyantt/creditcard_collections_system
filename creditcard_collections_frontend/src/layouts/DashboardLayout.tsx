import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Home, CreditCard, FileText, Settings } from "lucide-react"
import { Link, Outlet } from "react-router-dom"

export default function DashboardLayout() {
  return (
    <div className="flex min-h-screen bg-gray-50">
      <aside className="w-64 bg-white shadow-md">
        <div className="p-4 font-bold text-xl">CollectionsSys</div>
        <nav className="flex flex-col space-y-2 p-4">
          <Link to="/dashboard" className="flex items-center gap-2 text-gray-700 hover:text-black">
            <Home className="h-4 w-4" /> Overview
          </Link>
          <Link to="/dashboard/collections" className="flex items-center gap-2 text-gray-700 hover:text-black">
            <CreditCard className="h-4 w-4" /> Collections
          </Link>
          <Link to="/dashboard/reports" className="flex items-center gap-2 text-gray-700 hover:text-black">
            <FileText className="h-4 w-4" /> Reports
          </Link>
          <Link to="/dashboard/settings" className="flex items-center gap-2 text-gray-700 hover:text-black">
            <Settings className="h-4 w-4" /> Settings
          </Link>
        </nav>
      </aside>

      <main className="flex-1 p-8">
        <Card className="shadow-sm">
          <CardContent>
            <Outlet />
          </CardContent>
        </Card>
      </main>
    </div>
  )
}
