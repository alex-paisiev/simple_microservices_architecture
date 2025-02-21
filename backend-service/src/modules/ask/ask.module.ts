import { HttpModule } from '@nestjs/axios';
import { Module } from '@nestjs/common';
import { AskController } from './ask.controller';
import { AskService } from './ask.service';

@Module({
  imports: [HttpModule],
  controllers: [AskController],
  providers: [AskService],
})
export class AskModule {}
