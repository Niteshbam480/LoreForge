import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import { useAuth } from "../context/AuthContext";


export default function Login() {


    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const { login } = useAuth();
    const navigate = useNavigate();





    async function handleSubmit() {
        try {
            const response = await api.post("/auth/login", { email, password })
            const token = response.data.access_token
            login(token);
            navigate("/dashboard");

        }
        catch (error) {
            setError("Invalid email or password");
        }

    }

    return (
        <div className="login-wrapper">
            <h1>Login</h1>
            <input
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleSubmit}>Login</button>
            {error && <p>{error}</p>}
        </div>
    )


}