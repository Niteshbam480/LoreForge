import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import { useAuth } from "../context/AuthContext";



export default function Dashboard() {
    const [universes, setUniverses] = useState([]);
    const [loading, setLoading] = useState(true);
    const { logout } = useAuth();
    const navigate = useNavigate();


    useEffect(() => {
        async function fetchUniverses() {
            try {
                const response = await api.get("/universes/")
                setUniverses(response.data);
            } catch (error) {
                console.error("Error fetching universes:", error);
            } finally {
                setLoading(false);
            }
        }

        fetchUniverses();
    }, []);

    if (loading) {
        return (
            <div>
                Loading...
            </div>
        )
    }
    return (
        <div>
            <h1>My Universes </h1>
            <button onClick={() => { logout(); navigate("/login") }}>Logout</button>
            {
                universes.map((universe) => (
                    <div key={universe.id}>
                        <h2>{universe.name}</h2>
                        <p>{universe.description}</p>
                    </div>
                ))
            }
        </div>
    )

}