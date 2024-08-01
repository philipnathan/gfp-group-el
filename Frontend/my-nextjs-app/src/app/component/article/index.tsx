import SosialMedia from "./sosialmedia";

export default function ArticleDash() {
  return (
    <>
      <h1 className="flex items-center justify-center font-bold text-custom-green p-10">
        Article & Tips
      </h1>
      <div className="bg-white px-10">
        <div className="grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-3">
          {/* Article 1 */}
          <div className="text-custom-steel-blue p-10 bg-custom-Gunmetal rounded-lg transition-transform duration-500 hover:scale-105">
            <p className="font-bold">Article satu</p>
            <br />
            <p>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Recusandae consectetur laudantium officiis asperiores consequuntur
              quae eius debitis voluptates ipsam, reiciendis sint consequatur
              maiores exercitationem non! Error molestias possimus reprehenderit
              libero.
            </p>
            <br />
            <button className="border border-custom-steel-blue p-2 rounded hover:scale-105">
              Read More
            </button>
          </div>

          {/* Article 2 */}
          <div className="text-custom-steel-blue p-10 bg-custom-Gunmetal rounded-lg transition-transform duration-500 hover:scale-105">
            <p className="font-bold">Article dua</p>
            <br />
            <p>
              Lorem, ipsum dolor sit amet consectetur adipisicing elit.
              Doloremque, voluptatum quis. Cupiditate delectus voluptatem
              distinctio quia quam debitis veniam minima reprehenderit molestiae
              ut, provident quaerat eaque quod praesentium sapiente qui?
            </p>
            <br />
            <button className="border border-custom-steel-blue p-2 rounded hover:scale-105">
              Read More
            </button>
          </div>

          {/* Article 3 */}
          <div className="text-custom-steel-blue p-10 bg-custom-Gunmetal rounded-lg transition-transform duration-500 hover:scale-105">
            <p className="font-bold">Article tiga</p>
            <br />
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis,
              sint eveniet, delectus modi beatae ducimus ex exercitationem, ut
              distinctio dolorem porro molestiae animi saepe nihil. Fugit maxime
              facere voluptatum ex.
            </p>
            <br />
            <button className="border border-custom-steel-blue p-2 rounded hover:scale-105">
              Read More
            </button>
          </div>
        </div>
        <div className="bg-white py-10 text-custom-steel-blue">
  <div className="bg-custom-light-blue py-10">
    <h2 className="p-10 text-center text-4xl">CREATE YOUR OWN SHOP</h2>
    <div className="flex flex-col items-center justify-center">
      <p className="text-center px-10 md:px-40 lg:px-80">
        It’s as easy as 1,2,3 to open your own shop on Made From Recycled and start selling your products. It’s FREE to list, you’ll get your own bespoke shop page with loads of functionality, receive instant payments for your sales and pay one of the lowest fees on the market.
      </p>
      <button className="mt-5 bg-custom-Gunmetal p-5 border items-center rounded-lg hover:bg-custom-Gunmetal/80 hover:scale-105">
        OPEN YOUR SHOP NOW
      </button>
    </div>
  </div>
</div>
<SosialMedia/>
      </div>
    </>
  );
}
