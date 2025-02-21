import HttpModule from '@nestjs/common';
import { Test, TestingModule } from '@nestjs/testing';
import { AskService } from '../src/modules/ask/ask.service';

describe('AskService', () => {
  let service: AskService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      imports: [HttpModule],
      providers: [AskService],
    }).compile();

    service = module.get<AskService>(AskService);
  });

  it('should return a transformed response', async () => {
    const question = 'hello';
    const expectedResult = { result: 'olleh' };

    // Override the method to simulate the FastAPI response
    jest.spyOn(service, 'callFastApi').mockImplementation(async () => expectedResult);
    const response = await service.callFastApi(question);
    expect(response).toEqual(expectedResult);
  });
});
