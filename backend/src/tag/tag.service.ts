import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class TagService {
  private readonly db: any;

  constructor() {
    const filePath = path.resolve(process.cwd(), 'src', 'tag', 'db.json');
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    this.db = JSON.parse(fileContent);
  }

  getTaggedContent(tag: string): string[] {
    const tagData = this.db.tags[tag];
    if (!tagData) {
      return [];
    }

    let documents = [...tagData.documents];
    for (const subTag in tagData.subTags) {
      documents = [...documents, ...this.getTaggedContent(subTag)];
    }

    return documents;
  }
}
