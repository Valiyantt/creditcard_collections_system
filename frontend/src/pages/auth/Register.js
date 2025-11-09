import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
export default function Register() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");
    const [error, setError] = useState(null);
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Placeholder for backend integration
            console.log("Registering:", { name, email, password });
            navigate("/login");
        }
        catch (err) {
            setError("Registration failed");
        }
    };
    return (_jsx("div", { className: "flex items-center justify-center min-h-screen bg-gray-50", children: _jsxs(Card, { className: "w-full max-w-md", children: [_jsx(CardHeader, { children: _jsx(CardTitle, { className: "text-center text-2xl font-semibold", children: "Create Account" }) }), _jsxs(CardContent, { children: [_jsxs("form", { onSubmit: handleSubmit, className: "space-y-4", children: [_jsxs("div", { children: [_jsx("label", { className: "block mb-1 text-sm font-medium", children: "Full Name" }), _jsx(Input, { placeholder: "John Doe", value: name, onChange: (e) => setName(e.target.value), required: true })] }), _jsxs("div", { children: [_jsx("label", { className: "block mb-1 text-sm font-medium", children: "Email" }), _jsx(Input, { type: "email", placeholder: "you@example.com", value: email, onChange: (e) => setEmail(e.target.value), required: true })] }), _jsxs("div", { children: [_jsx("label", { className: "block mb-1 text-sm font-medium", children: "Password" }), _jsx(Input, { type: "password", placeholder: "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", value: password, onChange: (e) => setPassword(e.target.value), required: true })] }), error && _jsx("p", { className: "text-red-600 text-sm", children: error }), _jsx(Button, { type: "submit", className: "w-full", children: "Register" })] }), _jsxs("p", { className: "text-sm text-center mt-4", children: ["Already have an account?", " ", _jsx(Link, { to: "/login", className: "text-blue-600 hover:underline", children: "Login" })] })] })] }) }));
}
