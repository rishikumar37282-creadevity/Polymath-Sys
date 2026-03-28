import { defineCollection, z } from 'astro:content';

const roadmapCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    phase: z.string().optional(),
    description: z.string().optional(),
    lastUpdated: z.date().optional(),
  }),
});

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    author: z.string(),
    image: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

const newsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    source: z.string(),
    url: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'roadmap': roadmapCollection,
  'blog': blogCollection,
  'news': newsCollection,
};
