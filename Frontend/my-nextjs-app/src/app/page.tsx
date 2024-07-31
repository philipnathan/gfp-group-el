import Image from "next/image";
import NavbarPage from "./component/navbar";
import HomeDashboard from "./component/homedash";
import FooterDash from "./component/footer";
import ArticleDash from "./component/article";
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
