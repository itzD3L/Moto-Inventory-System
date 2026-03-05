'use client';
import { useTheme } from "next-themes";

export default function Settings() {
    const { theme, setTheme } = useTheme();

    return (
        <div>
            <h1>Settings</h1>

            <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>
                {theme === "dark" ? "Light" : "Dark"}
            </button>
        </div>
    )
}