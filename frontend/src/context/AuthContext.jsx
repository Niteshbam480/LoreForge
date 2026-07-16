import { useState, useContext, createContext } from 'react';


export const AuthContext = createContext()

export default function AuthProvider({ children }) {
    const [token, setToken] = useState(localStorage.getItem("token"));

    const login = (newToken) => {
        localStorage.setItem("token", newToken);
        setToken(newToken);
    }

    const logout = () => {
        localStorage.removeItem("token");
        setToken(null);
    }

    return (
        <AuthContext.Provider value={{ token, login, logout }}>{children}</AuthContext.Provider>
    )
}

export function useAuth() {
    return useContext(AuthContext);
}