'use client';
import Hero from "./components/Hero";
import Form from "./components/Form";
import PetCards from "./components/petCards";

export default function Home() {
  return (
    <div>
      <Hero />
      <Form />
      <PetCards />
    </div>
  );
}
