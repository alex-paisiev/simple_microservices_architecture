import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AskModule } from './modules/ask/ask.module';


@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    AskModule,
  ],
})
export class AppModule {}
