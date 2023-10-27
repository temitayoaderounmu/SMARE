import authorsData from "@/assets/fakedata/authors.json";
import type { Author } from "@/lib/models/author";
import { NextRequest, NextResponse } from "next/server";

export async function GET (
  request: NextRequest,
  {
    params,
  }: {
    params: { id: string };
  }
) {
  const { id } = params;
  const index = Number(id); // in this simple example we use id as index
  const someAuthor: Author = authorsData.objects[index];
  if (someAuthor) {
    return NextResponse.json(someAuthor);
  }
  return NextResponse.json({ error: "Author not found" } as ApiError, {
    status: 404,
  });
}
