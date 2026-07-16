import { useAuth } from "../context/AuthContext";
import { Navigate } from "react-router-dom";





export default function ProtectedRoute({ children }) {
    const { token } = useAuth();
    if (!token) {
        return <Navigate to="/login" />;
    }
    else { return children; }
}