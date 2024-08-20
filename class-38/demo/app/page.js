'use client';
import Hero from "./components/Hero";
import Form from "./components/Form";
import PetCards from "./components/petCards";
import Head from "./head";

// export const metadata = {
//   title: "About us page",
//   description : "welcome to about us page"
// }

export default function Home() {
  return (
    <div>
      <Head title="Pets App"/>
      <Hero />
      <Form />
      <PetCards />
    </div>
  );
}
