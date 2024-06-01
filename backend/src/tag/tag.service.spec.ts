import { Test, TestingModule } from '@nestjs/testing';
import { TagService } from './tag.service';
import * as fs from 'fs';

jest.mock('fs');

describe('TagService', () => {
  let service: TagService;

  beforeEach(async () => {
    (fs.readFileSync as jest.Mock).mockReturnValue(JSON.stringify({
      tags: {
        animals: {
          documents: ['http://example.com/doc1', 'http://example.com/doc2'],
          subTags: {
            mammals: {
              documents: ['http://example.com/doc3'],
              subTags: {}
            },
            birds: {
              documents: ['http://example.com/doc4'],
              subTags: {}
            }
          }
        }
      }
    }));

    const module: TestingModule = await Test.createTestingModule({
      providers: [TagService],
    }).compile();

    service = module.get<TagService>(TagService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

  it('should return documents for a tag', () => {
    expect(service.getTaggedContent('animals')).toEqual([
      'http://example.com/doc1',
      'http://example.com/doc2',
      'http://example.com/doc3',
      'http://example.com/doc4',
    ]);
  });
});
