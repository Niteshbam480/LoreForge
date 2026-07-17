import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import { useAuth } from "../context/AuthContext";



export default function Dashboard() {
    const [universes, setUniverses] = useState([]);
    const [loading, setLoading] = useState(true);
    const [showForm, setShowForm] = useState(false);
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
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

    async function handleSubmit() {
        try {
            const response = await api.post("/universes/", { name, description })
            setUniverses([...universes, response.data]);
            setName("");
            setDescription("");
            setShowForm(false);
        } catch (error) {
            alert("Failed to create universe.")
        }
    }

    return (
        <div>
            <h1>My Universes </h1>
            {
                universes.map((universe) => (
                    <div key={universe.id}>
                        <h2>{universe.name}</h2>
                        <p>{universe.description}</p>
                    </div>
                ))
            }
            <button onClick={() => { setShowForm(!showForm) }}>Create New Universe</button>
            {showForm && (
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Name</label>
                        <input
                            placeholder="Name"
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                    </div>

                    <div>
                        <label>Description</label>
                        <input
                            placeholder="description"
                            type="text"
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                        />
                    </div>

                    <button type="submit">Submit</button>
                </form>
            )}

            <div>
                <button onClick={() => { logout(); navigate("/login") }}>Logout</button>
            </div>
        </div>
    )

}