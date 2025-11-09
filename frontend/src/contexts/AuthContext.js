import { jsx as _jsx } from "react/jsx-runtime";
import { createContext, useContext, useState } from "react";
const dummyUser = {
    name: "Test User",
    email: "test@example.com",
    password: "Test1234", // <- your dummy password
};
const AuthContext = createContext({
    user: null,
    login: () => false,
    logout: () => { },
});
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(dummyUser); // <- pre-populated
    const login = (email, password) => {
        if (email === dummyUser.email && password === dummyUser.password) {
            setUser(dummyUser);
            return true;
        }
        return false;
    };
    const logout = () => setUser(null);
    return (_jsx(AuthContext.Provider, { value: { user, login, logout }, children: children }));
};
export const useAuth = () => useContext(AuthContext);
