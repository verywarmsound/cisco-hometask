import { Controller, Get, Query } from '@nestjs/common';
import { TagService } from './tag.service';

@Controller('taggedContent')
export class TagController {
  constructor(private readonly tagService: TagService) {}

  @Get()
  getTaggedContent(@Query('tag') tag: string): string[] {
    return this.tagService.getTaggedContent(tag);
  }
}

