import { Body, Controller, HttpException, HttpStatus, Logger, Post } from '@nestjs/common';
import { AskService } from './ask.service';
import { AskDto } from './dto/ask.dto';

@Controller('ask')
export class AskController {
  private readonly logger = new Logger(AskController.name);

  constructor(private readonly askService: AskService) {}

  @Post()
  async ask(@Body() askDto: AskDto) {
    this.logger.log(`Received question: ${askDto.question}`);
    try {
      // Call the FastAPI service and return its response
      const result = await this.askService.callFastApi(askDto.question);
      return result;
    } catch (error) {
      this.logger.error('Error calling FastAPI service', error);
      throw new HttpException('Error processing request', HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }
}

