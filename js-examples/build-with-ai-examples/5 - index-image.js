import 'dotenv/config';
import {GoogleGenerativeAI} from '@google/generative-ai';
import chalk from 'chalk';
import fs from 'fs';

const key = process.env.API_KEY;
const genAI = new GoogleGenerativeAI(key);

//https://ai.google.dev/gemini-api/docs/api-overview#text_image_input

async function run() {
  const model = genAI.getGenerativeModel({model: 'gemini-pro-vision'});
  // const prompt = "Que marca é esse headphone?";
  //const prompt = "O que esta escrito no papel é verdadeiro, Que marca é esse headphone?";
  const image = {
    inlineData: {
      data: Buffer.from(fs.readFileSync("img/headphone e jbl.jpeg")).toString("base64"),
      mimeType: "image/png",
    },
  };
  const result = await model.generateContent([prompt, image]);
  const text = result.response.text();

  console.log({text})
}

run();