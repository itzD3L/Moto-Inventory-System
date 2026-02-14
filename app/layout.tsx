import type { Metadata } from "next";
import "@/app/globals.css";
import { poppins } from "@/app/ui/components/fonts";
import { ThemeProvider } from "@/app/ui/components/theme-provider";

export const metadata: Metadata = {
    title: {
        template: "%s | Motoshop",
        default: "Motosop"
    },
    description: "Motoshop Inventory System"
};

export default function RootLayout({
    children,
} : Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en" suppressHydrationWarning>
            <body className={`${poppins.className} antialiased`}>
                <ThemeProvider
                    attribute="class"
                    defaultTheme="system"
                    enableSystem
                >{children}</ThemeProvider>
            </body>
        </html>
    )
}
