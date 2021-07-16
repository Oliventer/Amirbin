<template>
    <div class="container mt-5">
        <select id="product_name" v-model="product_name" class="form-control">
            <option>Premium</option>
            <option>Unlimited</option>
        </select>
        <br>
        <button v-on:click="subscribe()" class="btn btn-primary">Buy Subscription</button>
    </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import {loadStripe} from '@stripe/stripe-js';

export default {
    data: function() {
        return {
            product_name: '',
        }
    },
    props: {

    },
    computed: {
        ...mapState('stripe_key', [
            'stripe_key', 'status_code', 'stripe_session_id'
            ]),
    },
    
    methods: {...mapActions('stripe_key', 
    ['GET_SUBSCRIPTION_KEY']),

    async subscribe() {
        await new Promise ((resolve) => {
                this.$store.dispatch('stripe_key/BUY_SUBSCRIPTION', this.product_name).then(result => {
                  resolve(result)
                })
              })
        const stripe = await loadStripe(this.stripe_key);
        if (this.status_code === 201)
        {
            return stripe.redirectToCheckout({sessionId: this.stripe_session_id})
        } 
    },

    },
    mounted() {
        this.GET_SUBSCRIPTION_KEY();
    
    },

};
</script>
