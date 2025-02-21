import type { ReactNode } from "react";
import ClientMantineProvider from "../components/ClientMantineProvider";
import "./globals.css";

export const metadata = {
  title: "Frontend Dashboard",
  description: "Next.js App Router with Mantine",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <ClientMantineProvider>
          {children}
        </ClientMantineProvider>
      </body>
    </html>
  );
}
