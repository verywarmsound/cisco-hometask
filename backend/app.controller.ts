import { Controller, Get, Query } from '@nestjs/common';
import { AppService } from './app.service';
import { TagService } from './src/tag/tag.service';


@Controller()
export class AppController {
  constructor(
    private readonly appService: AppService,
    private readonly tagService: TagService,
  ) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get('taggedContent')
  getTaggedContent(@Query('tag') tag: string): string[] {
    return this.tagService.getTaggedContent(tag);
  }
}
