import Image from "next/image";
import NavbarPage from "./components/navbar";
import HomeDashboard from "./components/homedash";
import FooterDash from "./components/footer";
import ArticleDash from "./components/article";
import Head from "next/head";

export default function Home() {
  return (
    <div>
      <Head>
        <title>PDC RYCYCLE</title>
        <link
          rel="stylesheet"
          href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css"
        />
      </Head>
      <NavbarPage />
      <div className="pt-20">
        <HomeDashboard />
        <ArticleDash />
        <FooterDash />
      </div>
    </div>
  );
}
