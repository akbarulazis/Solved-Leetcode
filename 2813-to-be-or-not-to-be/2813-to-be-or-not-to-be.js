/**
 * @param {string} val
 * @return {Object}
 */
const expect = function(val) {
    return {
    toBe:function(compareVal) {

        if (val === compareVal){
            return true
            }
        if (val !== compareVal){
            throw new Error("Not Equal")

        }
        

    },

    notToBe:function(compareVal){
        if (val !== compareVal){
            return true
        }
        if (val === compareVal){
            throw new Error("Equal")
        }

    }

    }

};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */