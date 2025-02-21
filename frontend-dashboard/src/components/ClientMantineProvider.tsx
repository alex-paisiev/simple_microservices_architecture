"use client";

import { MantineProvider } from "@mantine/core";
import type { ReactNode } from "react";

interface ClientMantineProviderProps {
  children: ReactNode;
}

export default function ClientMantineProvider({ children }: ClientMantineProviderProps) {
  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      {children}
    </MantineProvider>
  );
}
