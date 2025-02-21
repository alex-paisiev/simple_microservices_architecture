'use client';

import { Alert, Button, Container, Loader, TextInput, Title } from '@mantine/core';
import { FormEvent, useEffect, useState } from 'react';

interface ApiResponse {
  result: string;
}

export default function HomePage() {
  const [question, setQuestion] = useState<string>('');
  const [result, setResult] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      // Use NEXT_PUBLIC_API_URL environment variable to determine the backend URL
      const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000';
      console.log('Backend URL:', backendUrl);
      const response = await fetch(`${backendUrl}/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch response from backend');
      }

      const data: ApiResponse = await response.json();
      setResult(data.result);
    } catch (err) {
      console.error(err);
      setError('An error occurred while processing your request.');
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => {
    if (!result) {
      console.log('Hello from the frontend!');
    }
    else {
      console.log('Response rewuiryiuewyi:', result);
    };
  }, [result]);

  return (
    <Container size="sm" mt="xl">
      <Title align="center" mb="xl">Ask Your Question</Title>
      <form onSubmit={handleSubmit}>
        <TextInput
          label="Enter your question"
          placeholder="Type your question here..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
        />
        <Button type="submit" fullWidth mt="md" disabled={loading} className="submitButton">
          {loading ? <Loader size="sm" /> : 'Submit'}
        </Button>
      </form>
      {result && (
        <Alert title="Response" mt="md" color="green">
          {result}
        </Alert>
      )}
      {error && (
        <Alert title="Error" mt="md" color="red">
          {error}
        </Alert>
      )}
    </Container>
  );
}
