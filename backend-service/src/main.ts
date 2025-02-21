import { ValidationPipe } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.enableCors({
    origin: 'http://localhost:3000',
  });
  // Enable global validation for DTOs
  app.useGlobalPipes(new ValidationPipe());
  await app.listen(4000);
  console.log('Backend service running on port 4000');
}
bootstrap();


