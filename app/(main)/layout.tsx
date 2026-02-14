import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
// import theming here { ThemeProvider } from "next-themes";
import "@/app/globals.css";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata: Metadata = {
    title: {
        template: "%s | Motoshop",
        absolute: "Motoshop",
    },
    description: "Motoshop Inventory System",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body
                className={`${geistSans.variable} ${geistMono.variable} antialiased`}
            >
                {children}
                <h1>Hello World</h1>
            </body>
        </html>
    );
}
