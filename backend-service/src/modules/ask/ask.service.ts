import { HttpService } from '@nestjs/axios';
import { Injectable, Logger } from '@nestjs/common';
import { AxiosResponse } from 'axios';
import { firstValueFrom } from 'rxjs';

@Injectable()
export class AskService {
  private readonly logger = new Logger(AskService.name);

  constructor(private readonly httpService: HttpService) {}

  async callFastApi(question: string): Promise<any> {
    try {
      // Use an environment variable to configure the FastAPI URL if needed
      const fastApiUrl = process.env.FASTAPI_URL || 'http://localhost:5000/generate';
      this.logger.log(`Calling FastAPI at: ${fastApiUrl}`);

      // The FastAPI endpoint expects a "prompt" field; we pass the question as the prompt.
      const response: AxiosResponse = await firstValueFrom(
        this.httpService.post(fastApiUrl, { prompt: question })
      );

      this.logger.log('Received response from FastAPI service');
      return response.data;
    } catch (error) {
      this.logger.error('Error calling FastAPI /generate endpoint', error);
      throw error;
    }
  }
}
