from datetime import date

from django.shortcuts import render

# Create your views here.

all_posts = [
    {
        "slug": "San-Giobbe",
        "image": "Bellini.jpg",
        "author": "Edwin King'ori",
        "date": date(2023, 10, 23),
        "title": "San Giobbe Altarpiece by BELLINI, Giovanni(1430-1516, Italy)",
        "excerpt": "An exploration that describes Giovanni’s painting and his capability to develop a high renaissance Artwork.",
        "content": """
        The capability to conduct a reflective art analysis has become significant as most scholars seek to explore and scrutinize various elements 
        and principles used by artists to develop their artwork. Hence, this critique takes an interest in conducting a comprehensive exploration that describes Giovanni’s painting 
        and his capability to develop a high renaissance painting. For this reason, this analysis aims at exploring and studying the elements and principles used in “San Giobbe Altarpiece” painting done by Giovanni Bellini.
        The painting represents one of the most significant high renaissance Italian portraits done in the late 15th centuries,
        a period when most paintings were done on an oil and canvas medium. 
    
        Bellini’s work mainly conveys a meditative atmosphere as the painting’s movement, tranquility and dynamism resonate in viewers as they attempt to dwell in the image’s events
        and activities. The meditative mood in the painting is dictated through the utilization and configuration of elements
        such as realism, lighting, and coloring as well as principles such as movement, pattern, and proportion that are used to generate the overall outline of the painting. 
        These principles and elements generate an outstanding alignment of objects in the painting. For instance, Bellini chooses to generate an equal positive and negative spacing in the position of both the human figures and the building. In this case, he aligns the human figures in the lower half of the painting, 
        occupying the positive space while the upper half of the image is rendered with the display of the 15th century Italian architecture.
    
        The horizontal alignment and the distribution of visual weight of the human figures in the lower part of the painting creates a linear movement pattern from left to right, 
        which generates a symmetrical balance that makes the painting to feel stable. The viewers are received by the man in the far right, draped in a black robe with a rough texture.
        Bellini positions him in a vertical position and as he appears to be facing the viewers gesturing a welcoming stance. 
        On the other hand, Bellini utilizes geometry, which was a significant renaissance feature, to position the human figures in similar triangular shapes to form a solitary pyramid outline that attaches all human figures. 
        The geometrical outline of human figures creates a sense of stability as well as the conception of a meditative mood. In his case, Bellini positons the human figures in groups of three, each forming triangular shapes when conjoined with their heads except for Mary who sits on a throne holding a baby. 
        Thus, the angles of the men in the right and left parts of the painting as well as the three women sitting in the middle and Mary sitting on the throne, form a pyramid shape. 
    
        Bellini also combines warm light with high intensity colors to define the different objects and human figures as well as to generate some sense of realism in the painting. 
        The light originates from the building’s windows and floods the objects in the image with warmth and illuminates the human figures in different ways. 
        For instance, the light illuminated on the portrait’s objects creates a golden warmth tone to unify the human figures and in turn guide viewers to clearly recognize the sense of an absorbing and meditative atmosphere. 
        The high color intensity is evenly distributed through the portrait generating a smooth texture on the bodies of the human figures. 
    
    
        Additionally, the color intensity enables the viewers to distinguish the texture in the garments draped on the individuals. 
        For instance, Bellini chooses to distinguish the man in the far right, draped in a black robe by applying a low color intensity with uneven lighting, which generates a rough texture on his robe. on the other hand, 
        he decides to utilize high color intensity and even illumination of light on the other human figures to create a smooth texture on their garments.
        One of the most fascinating creativities in Bellini’s portrait is the rendering of the human bodies to generate humanism concept. Bellini chooses to paint two figures that are completely nude and are covered in soft and short garments. 
        He positions them on the opposite sides of the portrait, distinguishing and defining their bodies by flooding light and using high color intensity to create their two-dimensional forms. 
    
        In conclusion, Bellini creates a distinctive portrait that utilizes various high renaissance traits, such as the use of realism, utilization of geometry and generation of humanism. 
        Realism is generated through the natural illumination of light from the building’s windows as well as the linear alignment of the human figures on the altar to create a symmetrical balance of the overall portrait. 
        The utilization of geometry is generated through the triangular positioning of the human individuals in the groups of three except for Mary, 
        who is sitting on an elevated throne to signify authority and power. 
        The alignment of all human figures form a pyramid shape to illustrate their unification and development of a meditative atmosphere. 
        Additionally, the lighting and color intensity is evenly distributed through the portrait to create a smooth texture on both the garments and the rendered bodies of two men who are nearly nude. Bellini has creatively utilized the renaissance traits to create a meditative atmosphere.
"""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpeg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "lion.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
