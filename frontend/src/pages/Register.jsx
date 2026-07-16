import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import { useAuth } from "../context/AuthContext";



export default function Register() {

    const { login } = useAuth();
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    async function handleSubmit() {
        try {
            await api.post("/auth/register", { email, username, password })
            const response = await api.post("/auth/login", { email, password })
            const token = response.data.access_token
            login(token);
            navigate("/dashboard");
        }
        catch (error) {
            setError("Invalid Credentials")
        }

    }

    return (
        <div className="register-wrapper">
            <h1>Register</h1>
            <input
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <input
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleSubmit}>Register</button>
            {error && <p>{error}</p>}

        </div>
    )

}