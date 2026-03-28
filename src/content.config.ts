import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const roadmapCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/roadmap" }),
  schema: z.object({
    title: z.string(),
    phase: z.string().optional(),
    description: z.string().optional(),
    lastUpdated: z.date().optional(),
    timeline: z.array(z.object({
      time: z.string(),
      label: z.string(),
    })).optional(),
    tabs: z.array(z.string()).optional(),
  }),
});

const blogCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/blog" }),
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
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/content/news" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string().optional(),
    author: z.string().optional(),
    link: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'roadmap': roadmapCollection,
  'blog': blogCollection,
  'news': newsCollection,
};
