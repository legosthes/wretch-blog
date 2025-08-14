import dropin from "braintree-web-drop-in";

console.log(dropin.create);

const BrainTreePayment = () => ({
  instance: null,

  ableToSubmit: false,

  init: async function () {
    const token = this.$el.dataset.token;
    console.log(this.$refs.dropin);
    // instance 是一個promise，但我不知道他什麼時候弄好
    // 設計等他好了，讓button從disabled變成可以按
    this.instance = await dropin.create({
      container: this.$refs.dropin,
      authorization: token,
    });

    // 等上面跑完的時候，ableToSubmit就會變成true
    // 然後用x-bind把這個綁在button的diabled上面
    this.ableToSubmit = true;
  },

  onSubmit() {
    console.log(this.instance);
  },
});

export { BrainTreePayment };
