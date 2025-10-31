import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
export default function Login() {
    const { login } = useAuth();
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await login(email, password);
            navigate("/dashboard");
        }
        catch (err) {
            setError(err.message);
        }
    };
    return (_jsx("div", { className: "flex items-center justify-center min-h-screen bg-gray-50", children: _jsxs(Card, { className: "w-full max-w-md", children: [_jsx(CardHeader, { children: _jsx(CardTitle, { className: "text-center text-2xl font-semibold", children: "Sign In" }) }), _jsxs(CardContent, { children: [_jsxs("form", { onSubmit: handleSubmit, className: "space-y-4", children: [_jsxs("div", { children: [_jsx("label", { className: "block mb-1 text-sm font-medium", children: "Email" }), _jsx(Input, { type: "email", placeholder: "you@example.com", value: email, onChange: (e) => setEmail(e.target.value), required: true })] }), _jsxs("div", { children: [_jsx("label", { className: "block mb-1 text-sm font-medium", children: "Password" }), _jsx(Input, { type: "password", placeholder: "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", value: password, onChange: (e) => setPassword(e.target.value), required: true })] }), error && _jsx("p", { className: "text-red-600 text-sm", children: error }), _jsx(Button, { type: "submit", className: "w-full", children: "Login" })] }), _jsxs("p", { className: "text-sm text-center mt-4", children: ["Don\u2019t have an account?", " ", _jsx(Link, { to: "/register", className: "text-blue-600 hover:underline", children: "Register" })] })] })] }) }));
}
