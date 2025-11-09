import { createContext, useContext, useState, ReactNode } from "react";

interface User {
  name: string;
  email: string;
  password: string;
}

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => boolean;
  logout: () => void;
}

const dummyUser: User = {
  name: "Test User",
  email: "test@example.com",
  password: "Test1234", // <- your dummy password
};

const AuthContext = createContext<AuthContextType>({
  user: null,
  login: () => false,
  logout: () => {},
});

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(dummyUser); // <- pre-populated

  const login = (email: string, password: string) => {
    if (email === dummyUser.email && password === dummyUser.password) {
      setUser(dummyUser);
      return true;
    }
    return false;
  };

  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
